import React, {useState, useEffect} from 'react';
import { Link, useParams } from 'react-router-dom';

const NotePage = () => {

    let match = useParams()

    // useEffect

    return (
        <div>
            <h1>Single note {match.id}</h1>
        </div>
    )
}

export default NotePage
