import { useEffect, useState } from "react";
import {Box, Container, TextField} from "@mui/material"
import { useOutletContext } from "react-router-dom";

import AnimeCard from './AnimeCard'

function AnimeContainer() {
    const {animes, setAnimes, onRemoveAnime, onUpdateAnime} = useOutletContext()

    const [search, setSearch] = useState("")
    
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
    function handleSearchChange(event) {
        setSearch(event.target.value)
    }
    const filteredAnimes = animes.filter((anime) => {
        const lowerCaseAnimeName = anime.name.toLowerCase()
        const lowerCaseSearch = search.toLowerCase()
        
        return lowerCaseAnimeName.includes(lowerCaseSearch)
    })

    return (
        <div>
            <Box>
                <TextField
                id="search"
                label='Search...'
                variant="outlined"
                margin="normal"
                onChange={handleSearchChange}
                />
            </Box>
            <Container>
            {filteredAnimes.map(anime => <AnimeCard key={anime.id} anime={anime} onRemoveAnime={onRemoveAnime} onUpdateAnime={onUpdateAnime}/>)}
            </Container>
        </div>
    )
}

export default AnimeContainer