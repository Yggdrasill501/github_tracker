handleSubmit = item => {
    this.toggle();
    if (item.id) {
    axios
        .put(`http://localhost:8000/webapi/accounts/${item.id}/`, item)
        .then(res => this.refreshList());
    return;
    }
    axios
      .post("http://localhost:8000/webapi/accounts/", item)
      .then(res => this.refreshList());
};
handleDelete = item => {
    axios
        .delete(`http://localhost:8000/webapi/accounts/${item.id}`)
        .then(res => this.refreshList());
};
