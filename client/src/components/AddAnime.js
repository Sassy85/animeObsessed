import React, {useEffect, useState} from "react";
import { Box, Button, Container, TextField} from '@mui/material'
import { useOutletContext, useNavigate} from "react-router-dom";

function AddAnime() {
    const {onNewAnime} = useOutletContext()
    const [name, setName] = useState("")
    const [image, setImage] = useState("")
    const [summary, setSummary] = useState("")
    const [numEpisodes, setNumEpisodes] = useState("")
    const [completed, setCompleted] = useState("")
    const [likes, setLikes] = useState("")
    const navigate = useNavigate()

    function nameChange(event) {
        setName(event.target.value)
    }

    function imageChange(event) {
        setImage(event.target.value)
    }

    function summaryChange(event) {
        setSummary(event.target.value)
    }

    function numEpisodesChange(event) {
        setNumEpisodes(event.target.value)
    }

    function completedChange(event) {
        setCompleted(event.target.value)
    }

    function likesChange(event) {
        setLikes(event.target.value)
    }

    function handleSubmit(event) {
        event.preventDefault()
        const anime = {
            name, 
            image, 
            summary, 
            num_episodes: numEpisodes,
            completed,
            likes
            // id: Math.floor(Math.random() * 1000)
        }
        //make request to server

        fetch('/animes', {
            method: "POST", 
            headers: {
                "Content-Type": "application/json"
            }, 
            body: JSON.stringify(anime)
        }).then((r) => r.json())
        .then((newAnime) => {
            onNewAnime(newAnime)
            setName("")
            setImage("")
            setSummary("")
            setNumEpisodes("")
            setCompleted("")
            setLikes("")
            navigate("/animes")
        })

    }

    return (
        <div>
            <Container>
                <form className="animeForm" autoComplete="off" onSubmit={handleSubmit}>
                    <h3>Add New Anime</h3>

                    <Box>
                        <TextField
                        id="name"
                        label='Name'
                        variant="outlined"
                        required
                        value={name}
                        onChange={nameChange}
                        />
                    </Box>

                    <Box>
                        <TextField
                        id="image"
                        label='Image'
                        variant="outlined"
                        required
                        value={image}
                        onChange={imageChange}
                        />
                    </Box>

                    <Box>
                        <TextField
                        id="summary"
                        label='Summary'
                        variant="outlined"
                        required
                        value={summary}
                        onChange={summaryChange}
                        />
                    </Box>

                    <Box>
                        <TextField
                        id="num_episodes"
                        label='Number of episodes'
                        variant="outlined"
                        required
                        value={numEpisodes}
                        onChange={numEpisodesChange}
                        />
                    </Box>

                    <Box>
                        <TextField
                        id="completed"
                        label='Completed or Still Going?'
                        variant="outlined"
                        required
                        value={completed}
                        onChange={completedChange}
                        />
                    </Box>

                    <Box>
                        <TextField
                        id="likes"
                        label='Number of likes'
                        variant="outlined"
                        required
                        value={likes}
                        onChange={likesChange}
                        />
                    </Box>

                    <Button variant="contained" type="submit">Submit</Button>
                </form>
            </Container>
        </div>
    )
}

export default AddAnime