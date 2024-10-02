import React from 'react';
import {  Text, View, TextInput, Button, Image } from 'react-native';

function Entrada (){

  return (
    <View style={styles.container}>
      <View>
        <Image source={{uri: 'https://play-lh.googleusercontent.com/DiE5bE7DE22ULei0096ZDj_wZ1PvJJg19fZhcDxsMauglEVrQjnKa0YBptJUWvOPVQ=w240-h480-rw',}} style={{ width: 200, height: 200 }} />
      </View>
        <Text></Text>
        <Text style={styles.titulo}>SECURE MAIL</Text>
        <Text>Sua encomenda na palma da mão</Text>
      
        <TextInput placeholder='Login                                             ' style={styles.textInput} />
        
        <TextInput placeholder='Senha                                             ' style={styles.textInput}/>
       
    <View style={styles.alternativeLayoutButtonContainer}>
      <Button onPress="" title="Cadastrar" color="#1f65d0" />
    </View>
    <View style={styles.alternativeLayoutButtonContainer}> 
      <Button onPress="{this._onPressButton2}" title="Entrar" color="#1f65d0" />
    </View>
    <View style={styles.alternativeLayoutButtonContainer}> 
      <Button onPress="{this._onPressButton3}" title="Esqueci minha senha" color="#e7c43f" />
    </View>
      
    <View style={styles.rodape}>
      <Text>Aplicativo Android com React</Text>
      <Text>By Juliano, Marilza e Matheus</Text>
    </View>
         
  </View>
  );
}

export default Entrada;
