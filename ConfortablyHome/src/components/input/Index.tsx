import React, {forwardRef} from "react";
import {View, Text, TextInput} from 'react-native';
import {MaterialIcons} from '@expo/vector-icons'

import { Style }from "./Style";
import { themas } from "../../global/themes";

export const Input = forwardRef(()=>{
    return (
        <View style={Style.boxInput}>
             <Text style={Style.titleInput}>ENDEREÇO DE EMAIL</Text>
            <TextInput style={Style.textInput}  />
            <MaterialIcons name='email' size={30} color={themas.colors.gray}/>
        </View>
        )
})