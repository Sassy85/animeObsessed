import {Card} from '@mui/material'

function StreamCard({stream}) {
    const {id, image, name} = stream
    
    return (
        <Card id={id}>
            <div>
                <img src={image} alt={name} className='streamsImg'/>
                <h2>{name}</h2>
            </div>
        </Card>
    )
}

export default StreamCard