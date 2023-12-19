import { useState } from 'react'
import { Box, Container, TextField, Typography} from '@mui/material';
import {useFormik} from 'formik'
import * as yup from 'yup'

function Signup({setUser}) {

    const [signup, setSignup] = useState(true)

    const signupSchema = yup.object().shape({
        username: yup.string().min(2, 'Username is too Short!').max(20, 'Username is too long!').required('Username is Required!'),
        email: yup.string().email('Valid Email is Required!').required(),
        password: yup.string().min(5, 'Password is too Short!').max(20, 'Password is too long!').required('Password is Required!'), 
        passwordConfirmation: yup.string().required('Confirm Password').oneOf([yup.ref('password')], 'Passwords must match!')
    })

    const loginSchema = yup.object().shape({
        username: yup.string().required('Username Required'),
        password: yup.string().required('Password Required')
    })

    const formik = useFormik( {
        initialValues: {
            username: '',
            email: '',
            password: '', 
            passwordConfirmation: ''
        },
        validationSchema: signup ? signupSchema : loginSchema,
        onSubmit: ( values) => {
            const endpoint = signup ? '/users': '/login'
            fetch(endpoint, {
                method: 'POST', 
                headers: {
                    'Content-Type': 'application/json'
                }, 
                body: JSON.stringify(values)
            }).then( (resp) => {
                if (resp.ok) {
                    resp.json().then( ({user}) => {
                        setUser(user)
                        //navigate into site
                    })
                } else {
                    console.log('errors? handle them')
                }
            })
        }
    })

    function toggleSignup() {
        setSignup((currentSignup) => !currentSignup)
    }

    return (
        <div>
            <header className="title"><span>Anime Obsessed</span></header>

            <Container maxWidth='sm'>
                <button onClick={toggleSignup}>{signup ? 'Login!': 'Create New Account'}</button>
                <form onSubmit={formik.handleSubmit}>
                    
                    <TextField 
                    id="username" 
                    label="Username"
                    variant="outlined" 
                    error={!!formik.errors.username}
                    helperText={formik.errors.username}
                    required
                    value={formik.values.username}
                    onChange={formik.handleChange}
                    />

                    <Box>
                        {signup && <TextField
                            id='email'
                            label='Email'
                            variant='outlined'
                            error={!!formik.errors.email}
                            helperText={formik.errors.email}
                            required
                            value={formik.values.email}
                            onChange={formik.handleChange}
                        />}
                    </Box>

                    <Box>
                        <TextField 
                            id="password" 
                            label="Password"
                            type='password'
                            variant="outlined" 
                            error={!!formik.errors.password}
                            helperText={formik.errors.password}
                            required
                            value={formik.values.password}
                            onChange={formik.handleChange}
                        />
                    </Box>

                    <Box>
                        {signup && <TextField 
                            id="passwordConfirmation" 
                            label="Confirm Password"
                            type='password'
                            variant="outlined" 
                            error={!!formik.errors.passwordConfirmation}
                            helperText={formik.errors.passwordConfirmation}
                            required
                            value={formik.values.passwordConfirmation}
                            onChange={formik.handleChange}
                    />}
                    </Box>

                    <button variant='contained' type='submit'>Submit</button>
                </form>
            </Container>
        </div>
    )
}

export default Signup