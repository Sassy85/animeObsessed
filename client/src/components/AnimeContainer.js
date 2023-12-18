import { useEffect, useState } from "react";
import {Container} from "@mui/material"

import AnimeCard from './AnimeCard'

function AnimeContainer({animes, setAnimes, onRemoveAnime}) {
    useEffect(() => {
        fetch('/animes')
            .then((r) => {
                if (r.ok) {
                    r.json().then(setAnimes)
                }else{
                    console.log('NOT LOGGED IN!')
                }
            })
    }, [])
    return (
        <div>
            <Container>
            {animes.map(anime => <AnimeCard  key={anime.id} anime={anime} onRemoveAnime={onRemoveAnime}/>)}
            </Container>
        </div>
    )
}

export default AnimeContainer