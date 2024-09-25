import React, {useState, useEffect } from 'react';
import { Button, View} from 'react-native';

import './App.css';

// import Entrada from './paginas/Entrada';
import Login from './paginas/Login';
import Cadastro from './paginas/Cadastro';

export default function App() {

  const [pagina, setPagina]=useState(0)

  useEffect(
    ()=>{
      const url=window.location.href
      const res=url.split('?')
      setPagina(res[1])
    }
  
  )

  const linksPaginas=(p)=>{
    if(p==1){
      window.open('http/localhost:8082?1', '_self')
    } else if(p==2){
      window.open('http/localhost:8082?2', '_self')
    }
  }

  const retornarPagina=()=>{
      if(pagina==1){
        return <Login/>
      } else if(pagina==2){
        return <Cadastro/>
      } else{
        return  <View>
                  <Button onClick={()=>linksPaginas(1)} title='Entrar' />
                  <Button onClick={()=>linksPaginas(2)} title='Cadastro' /> 
                </View>
      }
  }

  return (
 
    <>
    {retornarPagina()}
    </>
    
   

  );

}

