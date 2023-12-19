import {Card} from '@mui/material'

function AnimeCard({anime, onRemoveAnime, onUpdateAnime}) {
    const {completed, id, image, likes, name, num_episodes, summary} = anime

    function handleDelete() {
        fetch(`/animes/${id}`, {
            method: "DELETE"
        })
        .then((r) => {
            if (r.ok) {
                onRemoveAnime(id)
            }
        })
    }

    function handleUpdate() {
        fetch(`/animes/${id}`, {
            method: "PATCH", 
            headers: {
                "Content-Type": "application/json"
            }, 
            body:JSON.stringify({likes: likes + 1})
        })
        .then((r) => r.json())
        .then((updatedAnime) => onUpdateAnime(updatedAnime))
    }

    return (
        <card id={id}>
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
                <button variant="contained" onClick={handleUpdate}>🌟🌟 {likes}</button>

                <button variant="contained" onClick={handleDelete}>☠️☠️</button>
            </div>
        </card>
    )
}

export default AnimeCard