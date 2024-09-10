import React from 'react';
import { StyleSheet, Text, SafeAreaView, ScrollView, StatusBar } from 'react-native';
const Lista = () => {
return (
<SafeAreaView style={styles.safecontainer}>
<ScrollView style={styles.containerScrollView}>
<Text style={styles.text}>
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque id dui sed nulla imperdiet scelerisque.
Integer malesuada facilisis nibh varius eleifend.
Cras a velit laoreet dui interdum consectetur.
Pellentesque volutpat placerat mauris in interdum.

.

</Text>
</ScrollView>
</SafeAreaView>
);
}
const styles = StyleSheet.create({
safecontainer: {
flex: 1,
paddingTop: StatusBar.currentHeight,
},
containerScrollView: {
backgroundColor: 'grey',
marginHorizontal: 20,
},
text: {
fontSize: 26,
},
});
export default Lista;