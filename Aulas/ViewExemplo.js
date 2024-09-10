import React from "react";
import { View, Text } from "react-native";
const ViewExemplo = () => {
return (
<View
style={{
flexDirection: "row",
height: 100,
padding: 20
}}
>
<View style={{ backgroundColor: "red", flex: 0.5 }} />
<Text>Olá, mundo!</Text>
</View>
);
};

export default ViewExemplo;