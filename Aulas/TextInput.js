import React, { useState } from 'react';
import { Text, TextInput, View } from 'react-native';
const App = () => {
const [text, setText] = useState('');
return (
<View style={{ padding: 10 }}>
<TextInput
style={{ height: 40 }}
placeholder="Type here to translate!"
onChangeText={newText => setText(newText)}
defaultValue={text}
keyboardType={'default'} //Define que deve abrir o teclado
/>
<View style={{ flexDirection: 'row' }}>
<Text style={{ padding: 10, fontSize: 42, flex: 1, flexWrap: 'wrap' }}>
{text}
</Text>
</View>
</View>
);
};
export default App;