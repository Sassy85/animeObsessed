import { NavLink } from 'react-router-dom';
import React from 'react'



function Nav() {
    return(
        <header>
            <header className='title' variant="h1" component="h2">Anime Obsessed</header>
            <nav>
                <NavLink to='/animes' end className="nav-link">Animes</NavLink>
                <NavLink to='/streams' className="nav-link">Streams</NavLink>
                <NavLink to='/animes/new' end className="nav-link">Add Anime</NavLink>
            </nav>
        </header>
    )
}

export default Nav 