import React, { Component } from 'react';

const list = [
  {
    "id": 1,
    "title": "Learn HTTP",
    "body": "I need to learn HTTP! All of it!"
  },
  {
    "id": 2,
    "title": "Second Item",
    "body": "Learn Django REST Framework"
  },
  {
    "id": 3,
    "title": "Third Item",
    "body": "Last todo. I don't know. Bleh."
  }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { list };
  }

  render() {
    return (
      <div>
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    )
  }
}

export default App;