import { ScrollView, StyleSheet, Text, View, Button, TextInput } from 'react-native';
import react, { useState } from 'react';


const Calculadora = () => {
  const [valor1, setValor1] = useState('');
  const [valor2, setValor2] = useState('');
  const [resultado, setResultado] = useState('');
  
  return (
    <ScrollView>
      <View style={styles.container}>
      <Text style={styles.titulo}>Calculadora de Somar</Text>
      
      <TextInput ref={input1 => { this.textInput1 = input1 }}
        placeholder='valor 1'
        keyboardType='numeric'
        onChangeText={valor1 => setValor1(valor1)}
      />
      <TextInput ref={input2 => { this.textInput2 = input2 }}
        placeholder='valor 2'
        keyboardType='numeric'
        onChangeText={valor2 => setValor2(valor2)} />
      </View>
      <View style={styles.botoes}>
        <Button
          title='Calcular'
          onPress={somar}
      />
      </View>
      <Text>{resultado ? resultado : ''}</Text>
      <Button style={styles.botoes}
        title='Limpar'
        onPress={limpar}
      ></Button>
    
    </ScrollView>
  );

    function somar() {
      if (valor1 > 0 && valor2 > 0) {
        setResultado(parseFloat(valor1) + parseFloat(valor2));
        console.log(resultado);
      } else {
        setResultado('');
      }
      }
      function limpar() {
        this.textInput1.clear();
        this.textInput2.clear();
        setResultado('');
      }
    };

const styles = StyleSheet.create(
  {
    container: {
      height: 200,
      flex: 1,
      backgroundColor: '#ebebeb',
      alignItems: 'center',
      justifyContent: 'center',
    },
    titulo: {
      color: 'black',
    },
    botoes: {
      height: 50,
    }
  }
);
export default Calculadora;
     