import React, { useEffect, useState } from "react";
import {Button,} from '@mui/material'
import { Switch, Route } from "react-router-dom";

import AnimeConainter from './AnimeContainer'
import Nav from './Nav'
import Signup from './Signup'
import StreamContainer from './StreamContainer'
import AddAnime from "./AddAnime";

function App() {
  const [user, setUser] = useState(null)
  const [animes, setAnimes] = useState([])

  useEffect(() => {
    fetch('/authorized')
    .then ((r) => {
      if(r.ok) {
        r.json().then((user) => setUser(user))
      }else {
        //handle what should happen if not logged in
        console.log('error')
      }
    })
  }, [])

  function handleLogout() {
    fetch('/logout', {
      method: "DELETE"
    }).then((r) => {
      if (r.ok) {
        //handle logout on frontend
        setUser(null)

      }
    })
  }

  if (!user) {
    return <Signup setUser={setUser}/>;
  }

  function onNewAnime(newAnime) {
    setAnimes((currentStateAnimes) => [newAnime, ...currentStateAnimes])
  }

  return <div>
    <Nav/>
    
    <Button variant="contained" onClick={handleLogout}>Logout</Button>

    <img src='client/src/Images/Streaming.jpeg' alt='Streaming On'/>

    <Button variant="contained">Streams</Button>

    <img src='client/src/Images/Animes.jpg' alt='Animes'/>

    <Button variant="contained">Animes</Button>

    <StreamContainer/>
    
    <AnimeConainter animes={animes} setAnimes={setAnimes}/>

    <AddAnime onNewAnime={onNewAnime}/>
  </div>
}

export default App;
