import axios from 'axios'
import {setAlert} from './alert'
import {
    SIGNUP_FAIL,
    SIGNUP_SUCCESS,
    LOGIN_FAIL,
    LOGIN_SUCCESS,
    LOGOUT
} from './types'


export const login = (email,password) => async dispatch =>{
    const config = {
        headers: {
            'Content-Type' : 'application/json'
        }
    }
    const body = JSON.stringify({email,password});
    try {
        const res = await axios.post('https://localhost:8000/api/token/',body,config)
        dispatch ({
            type:LOGIN_SUCCESS,
            payload: res.data
        })

        dispatch(setAlert('Authenticated Successfully!','success'));
    } catch (error) {
        dispatch({
            type:LOGIN_SUCCESS,
        });
        dispatch(setAlert('Error Authenticating','error'))
    }
}

export const signup = ({name,email,password,password2}) => async dispatch => {
    const config = {
        headers: {
            'Content-Type' : 'application/json'
        }
    }
    const body = JSON.stringify({name,email,password,password2});
    try {
        const res = await axios.post('https://localhost:8000/api/accounts/signup/',body,config)
        dispatch ({
            type:SIGNUP_SUCCESS,
            payload: res.data
        })

        dispatch(login(email,password));
    } catch (error) {
        dispatch({
            type:SIGNUP_FAIL,
        });
        dispatch(setAlert('Signup Failed','error'))
    }
}

export const logout = () => dispatch =>{
    dispatch(setAlert('logout successfully.','success'))
    dispatch({
        type:LOGOUT
    })
}
