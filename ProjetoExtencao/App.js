import * as React from 'react';
import { StyleSheet, } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Entrada from '/containers/Entrada';

const Stack = createNativeStackNavigator();

function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Entrada" component={Entrada} />
            </Stack.Navigator>
        </NavigationContainer>
);
};


const styles= StyleSheet.create({
    container: {
    flex: 1,
    textAlign: 'center',
    backgroundColor: '#6ab1dd' ,
    alignItems: 'center',
    justifyContent: 'center',
    fontsize: 20,
    },
    titulo: {
    margin: 20,
    fontWeight: 800,
    fontsize: 20,
    },
    cadastro: {
    margin: 10,
    fontWeight: 400,
    fontsize: 15,   
    left: 50,
    },
    textInput: {
    backgroundColor: '#eada6e' ,
    margin: 5,
    fontWeight: 500,
    fontsize: 16,
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

export default App;
