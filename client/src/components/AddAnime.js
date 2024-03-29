import React, {useEffect, useState} from "react";
import { Box, Container, TextField} from '@mui/material'
import { useOutletContext, useNavigate} from "react-router-dom";

function AddAnime() {
    const {onNewAnime} = useOutletContext()
    const [name, setName] = useState("")
    const [image, setImage] = useState("")
    const [summary, setSummary] = useState("")
    const [numEpisodes, setNumEpisodes] = useState("")
    const [stream, setStream] = useState("")
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

    function streamChange(event) {
        setStream(event.target.value)
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
            stream,
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
            setStream("")
            setLikes("")
            navigate("/animes")
        })

    }

    return (
        <div>
            <img src="https://static.zerochan.net/Mikasa.Ackerman.full.3909971.jpg" alt="Mikasa from Attak on Titan" className="addAnime"/>
            <div>
                <Container>
                    <form className="animeForm" autoComplete="off" onSubmit={handleSubmit}>
                        <h3>Add New Anime</h3>

                        <Box>
                            <TextField
                            id="name"
                            label='Name'
                            variant="outlined"
                            margin="normal"
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
                            margin="normal"
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
                            margin="normal"
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
                            margin="normal"
                            required
                            value={numEpisodes}
                            onChange={numEpisodesChange}
                            />
                        </Box>

                        <Box>
                            <TextField
                            id="completed"
                            label='Streaming On'
                            variant="outlined"
                            margin="normal"
                            required
                            value={stream}
                            onChange={streamChange}
                            />
                        </Box>

                        <Box>
                            <TextField
                            id="likes"
                            label='Number of likes'
                            variant="outlined"
                            margin="normal"
                            required
                            value={likes}
                            onChange={likesChange}
                            />
                        </Box>

                        <button variant="contained" type="submit">Submit</button>
                    </form>
                </Container>
            </div>
        </div>
    )
}

export default AddAnime