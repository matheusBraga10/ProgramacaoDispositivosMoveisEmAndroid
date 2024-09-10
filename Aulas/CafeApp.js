import React, { useState } from 'react';

import { Button, Text, View } from 'react-native';
const Cat = props => {
const [isHungry, setIsHungry] = useState(true);
return (
<View>
<Text>
I am {props.name}, and I am {isHungry ? 'hungry' : 'full'}!
</Text>
<Button
onPress={() => {
setIsHungry(false);
}}
disabled={!isHungry}
title={isHungry ? 'Give me some food, please!' : 'Thank you!'}
/>
</View>
);
};
const Cafe = () => {
return (
<>
<Cat name="Munkustrap" />
<Cat name="Spot" />
</>
);
};
export default Cafe;