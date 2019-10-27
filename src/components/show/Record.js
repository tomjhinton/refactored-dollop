import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'


class Record extends React.Component {


  constructor() {
    super()

    this.state = {
      record: {


      }

    }

  }


  componentDidMount() {
    console.log(this.props.match)
    axios.get(`/api/records/${this.props.match.params.id}`)
      .then(res => this.setState({record: res.data}))

  }

  render(){
    console.log(this)

    return(

      <div className='container'>
        <div className='columns is-multiline'>
          <div className='column'>
            <h1 className='title'> {this.state.record.title}</h1>
            <h2 className='title-2'> {this.state.record.artist}</h2>
          </div>
        </div>
        <div className='columns is-multiline'>
          <div className='column is-2'>
            <img src={this.state.record.cover}></img>
          </div>
          <div className='column'>
            {this.state.record.description}
          </div>
        </div>
      </div>







    )
  }
}
export default Record
