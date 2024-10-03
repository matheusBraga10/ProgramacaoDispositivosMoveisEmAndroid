import { Dimensions, StyleSheet } from "react-native";
import { themas } from "../../global/themes";

export const Style = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#BFDEE0',
        alignItems: 'center',
        justifyContent: 'center',
      },
      boxTop: {
        height:Dimensions.get('window').height/3,
        width:'100%',
        alignItems: 'center',
        justifyContent: 'center',
        
      },
      boxMid: {
        width:'100%',
        paddingHorizontal:37,
        height:Dimensions.get('window').height/4,
      },
      boxBottom: {
        width:'100%',
        height:Dimensions.get('window').height/3,
        alignItems:'center',
        
      },
      logo: {
        width:'100%',
      },
      titulo: {
        fontWeight: "bold",
        marginTop: 10,
        fontSize: 20,
      },
      titleInput:{
        marginLeft:5,
        color:themas.colors.gray,
        marginTop:20,
      },
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
      button: {
        width:200,
        height: 50,
        alignItems:'center',
        justifyContent:'center',
        backgroundColor:themas.colors.bsScreen,
        borderRadius:40,
      },
      textButtom:{
        fontSize: 20,
        fontWeight: "bold",

      },
      textBottom:{
        fontSize:16,
        color: themas.colors.gray,

      },
      textBottomCreate:{
        fontSize:18,
        color: "black",
        
      }
})