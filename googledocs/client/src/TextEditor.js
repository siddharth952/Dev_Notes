import { useCallback } from 'react'
import Quill from 'quill' // Not a react component
import "quill/dist/quill.snow.css"

const TOOLBAR_OPTIONS = [
    
]

export default function TextEditor() {
    
    const wrapperRef = useCallback((wrapper) => { // To make it always defined
        if (wrapper == null) return

        wrapper.innerHTML = ""
        const editor = document.createElement('div')
        wrapper.append(editor)
        new Quill(editor,{theme: 'snow'}) // Only one time
        
    },[])
    return <div className="container" ref={wrapperRef}></div>
}