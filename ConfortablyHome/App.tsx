import './gesture-handler';

import { StatusBar } from 'expo-status-bar';
import { StyleSheet } from 'react-native';
import Login from './src/pages/login/Index';

import Routes from './src/routes/Index.routes';
import { NavigationContainer } from '@react-navigation/native';

export default function App() {
  return (
    <NavigationContainer>
      <Routes/>
    </NavigationContainer>
    
  );
}

const styles = StyleSheet.create({
  container: {
  },
});
