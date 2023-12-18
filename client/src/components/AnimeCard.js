import {Button, Card} from '@mui/material'

function AnimeCard({anime, onRemoveAnime}) {
    const {completed, id, image, likes, name, num_episodes, summary} = anime

    function handleDelete() {
        //make request to the "/animes/:id"
        fetch (`/animes/${id}`, {
            method: "DELETE"
        })
        .then((r) => {
            if (r.ok) {
                onRemoveAnime(id)
            }
        })
    }

    return (
        <Card id={id}>
            <div>
                <h2>{name}</h2>
                <img src={image} alt={name} className='animeImg'/>
                <p>{summary}</p>
                <p>Number of Episodes {num_episodes}</p>
                <p>
                    {
                        completed ? 'Completed' : 'Still Going'
                    }
                </p>
                <p>Likes {likes}</p>

                <Button  variant="contained" onClick={handleDelete}>☠️☠️</Button>

                <Button  variant="contained">✏️</Button>
            </div>
        </Card>
    )
}

export default AnimeCard