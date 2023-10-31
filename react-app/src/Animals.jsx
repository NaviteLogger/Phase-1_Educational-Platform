function List(props) {
    return (
        <>
            {!props.animals ? (
                <div>Loading...</div>
            ) : props.animals.length > 0 ? (
                <ul>
                    {props.animals.map((animal) => {
                        return <li key={animal}>{animal}</li>;
                    })}
                </ul>
            ) : (
                <div>There are no animals on the list!</div>
            )}
        </>
    );
}

// or
function List(props) {
    return (
        <>
            {!props.animals && <div>Loading...</div>}
            {props.animals && props.animals.length > 0 && (
                <ul>
                    {props.animals.map((animal) => {
                        return <li key={animal}>{animal}</li>;
                    })}
                </ul>
            )}
            {props.animals && props.animals.length === 0 && <div>There are no animals in the list!</div>}
        </>
    );
}

function App() {
    const animals = [];

    return (
        <div>
            <h1>Animals: </h1>
            <List animals={animals} />
        </div>
    );
}
