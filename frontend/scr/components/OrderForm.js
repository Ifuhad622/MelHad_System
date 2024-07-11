import React, { useState } from 'react';

function OrderForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    product: '',
    quantity: 1,
    instructions: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission, e.g., send data to backend
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="name">Name</label>
        <input
          type="text"
          className="form-control"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input
          type="email"
          className="form-control"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="product">Product</label>
        <input
          type="text"
          className="form-control"
          id="product"
          name="product"
          value={formData.product}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="quantity">Quantity</label>
        <input
          type="number"
          className="form-control"
          id="quantity"
          name="quantity"
          value={formData.quantity}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="instructions">Special Instructions</label>
        <textarea
          className="form-control"
          id="instructions"
          name="instructions"
          value={formData.instructions}
          onChange={handleChange}
        />
      </div>
      <button type="submit" className="btn btn-primary">Submit Order</button>
    </form>
  );
}

export default OrderForm;
