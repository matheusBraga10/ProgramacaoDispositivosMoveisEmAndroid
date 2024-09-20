import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';
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
    
        <Text></Text>
        <Text style={styles.titulo}>SECURE MAIL</Text>
        <Text></Text>
        
        <TextInput placeholder='Login' style={styles.textInput} />
        <Text></Text>
        <TextInput placeholder='Senha' style={styles.textInput}/>
        <Text></Text>
        <Text style={styles.cadastro}>Cadastrar usuário</Text>
        <Text></Text>
        
      
    <View style={styles.alternativeLayoutButtonContainer}>
      <Button onPress={this._onPressButton} title="Cadastrar" />
      <Text></Text>
      <Button onPress={this._onPressButton2} title="Entrar" />
      <Text></Text>
      <Button onPress={this._onPressButton3} title="Esqueci minha senha" color="#841584" />
    </View>
    
      
      <View style={styles.rodape}>
      <Text>Aplicativo Android com React</Text>
      </View>
         
  </View>
  );
}
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5DC',
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
    margin: 10,
    fontWeight: '400',
    fontSize: 15,     
    left: 50,
  },
  alternativeLayoutButtonContainer: {
    margin: 5,

    
  },
  rodape: {

    top: 170,
    
  },
});



