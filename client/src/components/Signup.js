import { Button, InputLabel, TextField } from '@mui/material';
import {useFormik} from 'formik'
import * as yup from 'yup'

function Signup({setUser}) {

    const signupSchema = yup.object().shape({
        username: yup.string().min(2, 'Username is too Short!').max(20, 'Username is too long!').required('Required!'),
        email: yup.string().email('Invalid email!').required('Required!'),
        password:yup.string().min(6, 'Username is too Short!').max(20, 'Username is too long!').required('Required!')
    })

    const formik = useFormik( {
        initialValues: {
            username: '',
            email: '',
            password: ''
        },
        validationSchema: signupSchema,
        onSubmit: ( values) => {
            fetch('/users', {
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

    return (
        <div>
            {/*{formik.errors}*/}
            <form onSubmit={formik.handleSubmit}>
                <InputLabel htmlFor="username"></InputLabel>
                <TextField 
                id="username" 
                label="Username"
                variant="outlined" 
                required
                value={formik.values.username}
                onChange={formik.handleChange}
                />

                <InputLabel htmlFor="email"></InputLabel>                    <TextField 
                id="email" 
                label="Email"
                variant="outlined" 
                required
                value={formik.values.email}
                onChange={formik.handleChange}
                />

                <InputLabel htmlFor="password"></InputLabel>
                <TextField 
                id="password" 
                label="Password"
                type='password'
                variant="outlined" 
                required
                value={formik.values.password}
                onChange={formik.handleChange}
                />

                <Button variant='contained' type='submit'>Submit</Button>
            </form>
        </div>
    )
}

export default Signup