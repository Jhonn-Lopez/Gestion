import {View, Text, Image, TextInput, TouchableOpacity} from 'react-native'
import React from "react";
import { StatusBar } from "expo-status-bar";
import Animated, {FadeIn, FadeInDown, FadeInUp, FadeOut} from "react-native-reanimated";
import {useNavigation} from "@react-navigation/native";

export default function SignupScreen() {

    const navigation = useNavigation();

    return (
        <View className="bg-white h-full w-full">
            <StatusBar style="blue-950" />
            {/* Fondo (colocarle degrade para que se vea mejor el formulario) */}
            <Image className="h-full w-full absolute" source={require('../assets/images/background.png')} />

            {/* Logo
            <View className="flex-row justify-around w-full absolute">
                <Animated.Image entering={FadeInUp.delay(400).duration(1000).springify()} className="h-[225] w-[90]" source={require('../assets/images/logo.png')} />
            </View>
            */}


                {/* Titulo y formulario */}
            <View className="h-full w-full flex justify-around pt-48">
                {/* Titulo */}
                <View className="flex items-center">
                    <Text className="text-white font-bold tracking-wider text-5xl">
                        Sign Up
                    </Text>
                </View>

                {/* Formulario */}
                <View className="flex items-center mx-4 space-y-4">
                    <Animated.View entering={FadeInDown.delay(200).duration(1000).springify()} className="bg-white p-5 rounded-2xl w-full">
                        <TextInput placeholder='Name' placeholderTextColor={'gray'}/>
                    </Animated.View>
                    <Animated.View entering={FadeInDown.delay(400).duration(1000).springify()} className="bg-white p-5 rounded-2xl w-full">
                        <TextInput placeholder='Last Name' placeholderTextColor={'gray'}/>
                    </Animated.View>
                    <Animated.View entering={FadeInDown.delay(600).duration(1000).springify()} className="bg-white p-5 rounded-2xl w-full">
                        <TextInput placeholder='Email' placeholderTextColor={'gray'}/>
                    </Animated.View>


                    <Animated.View entering={FadeInDown.delay(800).duration(1000).springify()} className="bg-white p-5 rounded-2xl w-full ">
                        <TextInput placeholder='Password' placeholderTextColor={'gray'} secureTextEntry/>
                    </Animated.View>
                    <Animated.View entering={FadeInDown.delay(1000).duration(1000).springify()} className="bg-white p-5 rounded-2xl w-full mb-3">
                        <TextInput placeholder='Repeat Password' placeholderTextColor={'gray'} secureTextEntry/>
                    </Animated.View>
                    {/* Boton SignUp */}
                    <Animated.View entering={FadeInDown.delay(1200).duration(1200).springify()} className="w-full">
                        <TouchableOpacity
                            className="w-full /*color*/ bg-yellow-500 /*color*/ p-3 rounded-2xl mb-3">
                                <Text className="text-xl font-bold text-blue-950 text-center">
                                    SignUp
                                </Text>
                        </TouchableOpacity>
                    </Animated.View>
                    <Animated.View entering={FadeInDown.delay(1200).duration(1200).springify()} className="flex-row justify-center">
                        <Text className="text-white">Already have an account?  </Text>
                        <TouchableOpacity onPress={()=> navigation.push('Login')}>
                            <Text className="text-yellow-500 font-bold">Back to Login </Text>
                        </TouchableOpacity>
                    </Animated.View>

                </View>
            </View>
        </View>

    )
}