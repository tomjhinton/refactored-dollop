import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'
import 'bulma'
import './style.scss'

import Home from './components/common/Home'
import Navbar from './components/common/Navbar'
import Footer from './components/common/Footer'
import Record from './components/show/Record'

class App extends React.Component {
  constructor(){
    super()

    this.state = {
    }
  }

  componentDidMount() {

  }

  render() {
    return (

      <Router>
        <main>
          <Navbar />
          <Switch>
            <Route path="/records/:id" component={Record}/>
            <Route path="/" component={Home} />

          </Switch>

        </main>
        <footer>
          <Footer/>
        </footer>
      </Router>


    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
