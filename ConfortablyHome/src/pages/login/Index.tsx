import React, {useState} from 'react';
import { StatusBar } from 'expo-status-bar';
import { Text, View, Image, TextInput, TouchableOpacity, Alert, ActivityIndicator } from 'react-native';


import {MaterialIcons} from '@expo/vector-icons';
import { Style } from './Style';
import casaAzul from '../../assets/casaAzul.png'
import { themas } from '../../global/themes';

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)

  async function getLogin(){
    try{
      setLoading(true)
      if(!email || !password){
        return Alert.alert('Atenção','Informe os campos obrigatórios.')
      }
      setTimeout(()=>{
        if(email == 'matheusfbraga10@gmail.com' && password == '1234'){
          Alert.alert('Logado com sucesso.') 
        } else{
          Alert.alert('Usuario não cadastrado.')
        }
        setLoading(false)
       },1000)
    } catch(error){
      console.log(error)
    } 
  }

  return (
    <View style={Style.container}>
        <View style={Style.boxTop}>
          <Image source={casaAzul} style={Style.logo}  />
          <Text style={Style.titulo}>ConfortablyHome</Text>
        </View>
        <View style={Style.boxMid}>
            <Text style={Style.titleInput}>ENDEREÇO DE EMAIL</Text>
          <View style={Style.boxInput}>
            <TextInput style={Style.textInput} onChangeText={setEmail} />
            <MaterialIcons name='email' size={30} color={themas.colors.gray}/>
          </View>
            <Text style={Style.titleInput}>SENHA</Text>
          <View style={Style.boxInput}>
            <TextInput style={Style.textInput} onChangeText={setPassword}/>
            <MaterialIcons name='remove-red-eye' size={30} color={themas.colors.gray}/>
          </View>
        </View>
        <View style={Style.boxBottom}>
          <TouchableOpacity style={Style.button} onPress={getLogin}>
            {loading ? <ActivityIndicator color={themas.colors.primary} size='small' /> : <Text style={Style.textButtom}>Entrar</Text> }
          </TouchableOpacity>
        </View>
        <Text style={Style.textBottom} >Não possui conta? 
          <Text style={Style.textBottomCreate} > Faça aqui.</Text>
        </Text>
      <StatusBar style="auto" />
    </View>
  );
}



  

