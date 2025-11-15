function HelloComponent(){
    return(
        <div>
            <h1>
                React Hello
            </h1>
            <button onClick={() => {alert('Hello')}}>
                Click me
            </button>
        </div>
    )
}

export default HelloComponent