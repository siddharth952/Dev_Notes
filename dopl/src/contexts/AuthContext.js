import React, { useContext, useState, useEffect } from 'react'
import {auth} from '../firebase'
// Create auth context
const AuthContext = React.createContext()
// To use the context
export function useAuth() {
    return useContext(AuthContext)
}

export function AuthProvider({children}) {
    const [currentUser, setCurrentUser] = useState()
    function signup(email, password) {
        return auth.createUserWithEmailAndPassword(email, password)
    }


    useEffect(() => {
        const unsubscribe = auth.onAuthStateChanged(user => {
            setCurrentUser(user)
        })
        return unsubscribe
    },[])

    
    const value = {
        currentUser,
        signup
    }

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    )
}