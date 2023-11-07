from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            email = data['email']
            password = data['password']

            # Verifica si el usuario ya existe
            if User.objects.filter(email=email).exists():
                return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

            # Hash de la contraseña antes de guardarla en la base de datos
            password_hashed = make_password(password)

            user = User(email=email, name=data['name'], last_name=data['last_name'], password=password_hashed)
            user.save()

            # Autentica al usuario después del registro
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)

            return Response({'message': 'Registro exitoso'}, status=status.HTTP_201_CREATED)

        return Response({'error': 'Error de validación'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    if request.method == 'POST':
        data = request.data
        email = data.get('email')
        password = data.get('password')

        print(f'Intento de inicio de sesión con email: {email} y contraseña: {password}')  # Agrega esta línea

        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Las credenciales son válidas, inicia sesión en la sesión actual
            login(request, user)
            return Response({'message': 'Login exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)

