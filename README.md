#coastal connection gardens
# CoastalConnectionGardens

Costal Connections will serve as a full stack web application that tracks sales revenue, processes orders and updates inventory.

The data schema uses is as follows, a product will be created by the site owner, giving it a description and setting its cost and price within the price table. this will create a Cost of Inventory item which will record the cost of the quantity to add to the inventory table. The inventory table tracks the quantity of which products are on hand, and their cost associated to the bussiness owner.
when a customer is created their information is recorded and they process a customer_order which has a list of product ids and quantity associated with each product, date ordered will be created when finalized, and a fullfilled key of false. this will in turn create a sales instance, where the gross sale is calculated from the total of customer_order total_price and the net sales are recorded based on the cost of inventory at the time of the sale

this will be recorded as FIFO data first in first out, this will help in displaying a more accurate description of sales and their revenue and loss based on shelf life.
this will determine a more accurate COG cost of good

we will also record this with a weighted average, to account for variations of season and costs.