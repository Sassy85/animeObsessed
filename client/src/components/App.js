import React, { useEffect, useState } from "react";
import {Outlet} from "react-router-dom";

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
    setAnimes((currentStateAnimes) => [ ...currentStateAnimes, newAnime])
  }

  function onRemoveAnime(animeId) {
    setAnimes((currentsAnimes) => {
      return currentsAnimes.filter((anime) =>anime.id !== animeId)
    })
  }

  function onUpdateAnime(updatedAnime) {
    setAnimes((currentsAnimes) => {
      return currentsAnimes.map((anime) => {
        if (anime.id === updatedAnime.id) {
          return updatedAnime
        } else {
          return anime
        }
      })
    })
  }
  const context = {
    animes, 
    setAnimes, 
    onRemoveAnime, 
    onUpdateAnime, 
    onNewAnime
  }

  return <div>
    <Nav/>
    
    <button className='logout' onClick={handleLogout}>Logout</button>

    {/* <StreamContainer/>
    
    <AnimeConainter animes={animes} setAnimes={setAnimes} onRemoveAnime={onRemoveAnime} onUpdateAnime={onUpdateAnime}/>

    <AddAnime onNewAnime={onNewAnime}/> */}
    <Outlet context={context}/>
  </div>
}

export default App;
