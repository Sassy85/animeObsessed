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

  function onRemoveAnime(animeId) {
    console.log(animeId)
    setAnimes((currentsAnimes) => {
      return currentsAnimes.filter((anime) =>anime.id !== animeId)
    })
  }

  return <div>
    <Nav/>
    
    <Button variant="contained" onClick={handleLogout}>Logout</Button>

    <StreamContainer/>
    
    <AnimeConainter animes={animes} setAnimes={setAnimes} onRemoveAnime={onRemoveAnime}/>

    <AddAnime onNewAnime={onNewAnime}/>
  </div>
}

export default App;
