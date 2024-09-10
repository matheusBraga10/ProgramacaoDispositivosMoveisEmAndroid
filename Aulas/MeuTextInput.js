import React from "react";
import { SafeAreaView, StyleSheet, TextInput } from "react-native";
const MeuTextInput = () => {
const [texto, setTexto] = React.useState(null);
const [numero, setNumero] = React.useState(0);
return (
<SafeAreaView>
<TextInput
style={styles.meutextinput}
value={texto}
/>
<TextInput
style={styles.meutextinput}
onChangeText={setNumero}
value={numero}
keyboardType="numeric"
/>
</SafeAreaView>
);
};
const styles = StyleSheet.create({
meutextinput: {
marginTop: 100,
height: 40,
margin: 12,
borderWidth: 1,
},
});
export default MeuTextInput;