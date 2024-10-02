import { StyleSheet } from "react-native";
import { themas } from "../../global/themes";

export const Style = StyleSheet.create({
    boxInput:{
        width:'100%',
        height: 40,
        borderWidth:1,
        borderRadius:40,
        marginTop:10,
        alignItems: 'center',
        flexDirection: "row",
        paddingHorizontal: 10,
        backgroundColor:themas.colors.bsScreen,
        borderColor: themas.colors.bsScreen,
      },
      textInput:{
        height:'100%',
        width: '90%',
        borderRadius:40,
      },
      titleInput:{
        marginLeft:5,
        color:themas.colors.gray,
        marginTop:20,
      },
})