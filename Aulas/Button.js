import { StyleSheet, View, Button } from 'react-native';
export default function App() {
return (
<View style={styles.container}>
<Button
onPress={() => {
console.log('You tapped the button!!!');
}}
title="Press Me"
/>
</View>
);
}
const styles = StyleSheet.create({
container: {
flex: 1,
backgroundColor: '#fff',
alignItems: 'center',
justifyContent: 'center',
},
});