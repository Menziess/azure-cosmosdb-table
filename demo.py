import os

from azure.cosmosdb.table.tableservice import TableService
from dotenv import load_dotenv


load_dotenv()


def main():
    """Run main program."""
    table_service = TableService(
        account_name=os.getenv('ACCOUNT_NAME'),
        account_key=os.getenv('ACCOUNT_KEY')
    )

    table_service.create_table('tasktable')

    task = {
        'PartitionKey': 'feature',
        'RowKey': '001',
        'description': 'Take out the trash',
        'priority': 200
    }

    table_service.insert_entity('tasktable', task)

    task['priority'] = 250

    table_service.update_entity('tasktable', task)

    table_service.insert_or_replace_entity('tasktable', task)

    task = table_service.get_entity('tasktable', 'feature', '001')
    print(task.description)
    print(task.priority)

    table_service.delete_entity(
        'tasktable',
        task['PartitionKey'],
        task['RowKey']
    )

    table_service.delete_table('tasktable')


if __name__ == "__main__":
    main()
