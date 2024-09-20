import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, Button, Image } from 'react-native';
export default class App extends Component {

_onPressButton() {
  //Alert.alert('You tapped the button!'); //Somente funciona somente no IOS e Android
  alert('Usuario cadastrado com sucesso!');
  }
  _onPressButton2() {
    //Alert.alert('You tapped the button!'); //Somente funciona somente no IOS e Android
    alert('Passando para a proxima tela!');
  }
  _onPressButton3() {
      //Alert.alert('You tapped the button!'); //Somente funciona somente no IOS e Android
  alert('Uma solicitacao de alteracao de senha foi enviada para o seu email');
  }
  render() {
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
      <Button onPress={this._onPressButton} title="Cadastrar" color="#1f65d0" />
    </View>
    <View style={styles.alternativeLayoutButtonContainer}> 
      <Button onPress={this._onPressButton2} title="Entrar" color="#1f65d0" />
    </View>
    <View style={styles.alternativeLayoutButtonContainer}> 
      <Button onPress={this._onPressButton3} title="Esqueci minha senha" color="#e7c43f" />
    </View>
    
      
    <View style={styles.rodape}>
      <Text>Aplicativo Android com React</Text>
      <Text>By Juliano, Marilza e Matheus</Text>
    </View>
         
  </View>
  );
}
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    
    backgroundColor: '#5eafe1',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: 20,
    
  },
  titulo: {
    margin: 20,
    fontWeight: '800',
    fontSize: 20,
  },
  cadastro: {
    margin: 10,
    fontWeight: '400',
    fontSize: 15,     
    left: 50,
  },
  textInput: {
    backgroundColor: '#eada6e',
    margin: 5,
    fontWeight: '500',
    fontSize: 16,  
    top: 20,   
    
  },
  alternativeLayoutButtonContainer: {
    margin: 3,
    top: 70,
    width: 140,
     
  },
  rodape: {
    alignItems: 'center',
    justifyContent: 'center',
    top: 130,
    
  },
});



