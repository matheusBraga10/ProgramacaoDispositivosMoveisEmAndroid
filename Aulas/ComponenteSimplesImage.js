import React from 'react';

import { View, Image, StyleSheet } from 'react-native';
const styles = StyleSheet.create({
container: {
paddingTop: 50,
},
imagem: {
width: 50,
height: 50,
alignSelf: 'center'
}
});
const ComponenteSimplesImage = () => {
return (
<View style={styles.container}>
<Image
style={styles.imagem}
source={{
uri: 'https://reactnative.dev/img/tiny_logo.png',
}}
/>
</View>
);
}
export default ComponenteSimplesImage;