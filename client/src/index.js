import React from "react";
import App from "./components/App";
import "./index.css";
import { createRoot } from "react-dom/client";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import AnimeContainer from "./components/AnimeContainer";
import MainPage from "./components/MainPage";
import StreamContainer from "./components/StreamContainer";
import AddAnime from "./components/AddAnime";

const routes = [
    {
        path: "/", 
        element: <App/>, 
        children: [
            {
                path: "/home", 
                element: <MainPage/>
            },
            {
                path: "/animes", 
                element: <AnimeContainer/>,
            }, 
            {
                path: '/streams', 
                element: <StreamContainer/>
            }, 
            {
                path: '/animes/new', 
                element: <AddAnime/>
            }
        ]
    },
]

const router = createBrowserRouter(routes)

const container = document.getElementById("root");
const root = createRoot(container);
root.render(<RouterProvider router={router}/>);
