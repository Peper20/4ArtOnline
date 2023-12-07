import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import {Bottom} from "./components/Bottom"
import './App.css'

import { createStore } from 'redux'

const defaultState = {
  cash: 0 
}
const reducer = (state = defaultState, action)=>{
    switch(action.type){
      case "addC":
        return {...state, cash:state.cash +  action.playload}

      case "getC":
        return {...state, cash: state.cash - action.playload}

      default:
        return state
    }
}






function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <Provider store={store}> */}
      <BrowserRouter>
      <Routes>
        
        <Route path="/" element={<>
        
        <Bottom />
        
        </>} />
      </Routes>
    </BrowserRouter>
      {/* </Provider > */}
    </>
  )
}

export default App
