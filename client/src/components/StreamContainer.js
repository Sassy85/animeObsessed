import { useEffect, useState } from "react";
import {Container} from '@mui/material'

import StreamCard from './StreamCard'

function StreamContainer() {
    const [streams, setStreams] = useState([])

    useEffect(() => {
        fetch('/streams').then((r) => {
            if (r.ok) {
                r.json().then(setStreams)
            } else {
                console.log('NOT LOGGED IN')
            }
        })
    }, [])
    return (
        <div>
            <Container>
                {streams.map(stream => <StreamCard key={stream.id} stream={stream}/>)}
            </Container>
        </div>
    )
}

export default StreamContainer