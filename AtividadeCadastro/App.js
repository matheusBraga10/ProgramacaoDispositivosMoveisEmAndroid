import React, { Component } from 'react';
import { Alert, Button, StyleSheet, Text, View, TextInput } from 'react-native';
export default class ButtonBasics extends Component {
_onPressButton() {
//Alert.alert('You tapped the button!'); //Somente funciona somente no IOS e Android
alert('Usuário cadastrado com sucesso!');
}
_onPressButton2() {
  //Alert.alert('You tapped the button!'); //Somente funciona somente no IOS e Android
  alert('Você receberá novidades em seu e-mail!');
}
_onPressButton3() {
    //Alert.alert('You tapped the button!'); //Somente funciona somente no IOS e Android
alert('Não lhe enviaremos e-mail.');
}
render() {
return (
<View style={styles.container}>

<Text style={styles.titulo}>Cadastrar usuário:</Text>
<Text/>

<TextInput placeholder='Digite seu nome' style={styles.textInput} />
<TextInput placeholder='Digite seu Telefone' style={styles.textInput} />
<TextInput placeholder='Digite seu e-mail' style={styles.textInput} />
<TextInput placeholder='Digite seu endereço' style={styles.textInput} />
<TextInput placeholder='Digite seus interesses pessoais' style={styles.textInput} />

<View style={styles.alternativeLayoutButtonContainer}>
<Text style={styles.alternativeLayoutButtonContainer}>Deseja receber spam? </Text>
<Button onPress={this._onPressButton2} title="Sim" />
<Button onPress={this._onPressButton3} title="Não" color="#841584" />
</View>


<Button onPress={this._onPressButton} title="Cadastrar" />

</View>

);
}
}

const styles = StyleSheet.create({
    container: {
    flex: 1,
    justifyContent: 'center',
    },
    titulo: {
    margin: 20,
    fontWeight: 'bold',
    fontSize: 20,
    },
    alternativeLayoutButtonContainer: {
    margin: 20,
    flexDirection: 'row',
    },
    textInput: {
margin: 5,
    },
    });