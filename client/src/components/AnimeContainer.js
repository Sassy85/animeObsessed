import { useEffect, useState } from "react";
import {Container} from "@mui/material"
import { Grid } from "semantic-ui-react";
import { useOutletContext } from "react-router-dom";

import AnimeCard from './AnimeCard'

function AnimeContainer() {
    const {animes, setAnimes, onRemoveAnime, onUpdateAnime} = useOutletContext()
    
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
            {animes.map(anime => <AnimeCard key={anime.id} anime={anime} onRemoveAnime={onRemoveAnime} onUpdateAnime={onUpdateAnime}/>)}
            </Container>
        </div>
    )
}

export default AnimeContainer