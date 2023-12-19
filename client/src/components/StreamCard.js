import {Card} from '@mui/material'

function StreamCard({stream}) {
    const {id, image, name} = stream
    
    return (
        <card id={id}>
            <div>
                <img src={image} alt={name} className='streamsImg'/>
                <h2>{name}</h2>
            </div>
        </card>
    )
}

export default StreamCard