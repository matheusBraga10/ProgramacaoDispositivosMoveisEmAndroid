import React, { useState } from "react";
import { Text, StyleSheet } from "react-native";
const TextoAninhado = () => {
const [titulo, setTitulo] = useState("Texto do elemento filho");
const modificaTexto = () => {
setTitulo("Esse texto está sendo exibido pois o primeiro elemento de texto foi pressionado/tocado");
};
return (
<Text style={styles.baseText}>
<Text style={styles.titulo} onPress={modificaTexto}>
{titulo}
{"\n"}
{"\n"}
</Text>
</Text>
);
};
const styles = StyleSheet.create({
baseText: {
fontFamily: "Verdana",
marginTop: 50,
marginLeft: 10
},
titulo: {
marginTop: 10,
fontSize: 18,
fontWeight: "bold"
}
});
export default TextoAninhado;