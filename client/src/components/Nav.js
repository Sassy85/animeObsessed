import { NavLink } from 'react-router-dom';
import React, {useState} from 'react'
import {Typography } from "@mui/material";



function Nav() {
    return(
        <header>
            <Typography className='title' variant="h1" component="h2">Anime Obsessed</Typography>
            <nav>
                <NavLink to='/animes' end className="nav-link">Animes</NavLink>
                <NavLink to='/streams' className="nav-link">Streams</NavLink>
                <NavLink to='/animes/new' end className="nav-link">Add Anime</NavLink>
            </nav>
        </header>
    )
}

export default Nav 